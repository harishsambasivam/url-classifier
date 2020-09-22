import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { URLcheckerComponent } from './urlchecker.component';

describe('URLcheckerComponent', () => {
  let component: URLcheckerComponent;
  let fixture: ComponentFixture<URLcheckerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ URLcheckerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(URLcheckerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
