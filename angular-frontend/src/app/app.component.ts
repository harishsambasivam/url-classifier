import { Component } from "@angular/core";
import {
  FormBuilder,
  FormControl,
  FormGroup,
  Validators
} from "@angular/forms";
import {CheckurlService} from "../../src/app/checkurl.service"
import { prepareSyntheticListenerFunctionName } from '@angular/compiler/src/render3/util';

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.scss"]
})
export class AppComponent {
  resultemoji :any = ""; 
  result_message : string = "";
  phish:boolean = false;
  constructor(private fb: FormBuilder,private checkurl:CheckurlService) {}
  ngOninit() {
  }

  onSubmit(url: any){
    this.phish = false;
    this.resultemoji = "security";
    this.result_message = "Analyzing the URL.....";
      this.checkurl.checkUrl(url.url).subscribe(res => {
        console.log(res.data)
        if(res.data === "legitimate"){
          this.phish = false;
          this.resultemoji = "mood";
          this.result_message = "You can surf without any fear!!!";
          console.log("legitimate")
        }else if(res.data === "phish"){
          this.phish = true;
          this.resultemoji = "mood_bad";
          this.result_message = "oww!! phishing website!!!";
          console.log("phish")
        }
      });
  }
}
