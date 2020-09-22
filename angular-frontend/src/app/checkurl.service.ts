import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { Observable } from 'rxjs';
interface UserPostResponse {
  data: any
}
@Injectable({
  providedIn: 'root'
})


export class CheckurlService {

  constructor(private http:HttpClient) { }
  checkUrl(url: string): Observable<UserPostResponse> {
    console.log(`http://127.0.0.1:5000/checkurl?url=${url.toString()}`)
     return this.http.get<UserPostResponse>(`http://192.168.1.100:5000/checkurl?url=${url}`);
  }
}
