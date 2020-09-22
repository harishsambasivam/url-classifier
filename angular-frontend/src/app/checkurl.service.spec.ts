import { TestBed } from '@angular/core/testing';

import { CheckurlService } from './checkurl.service';

describe('CheckurlService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CheckurlService = TestBed.get(CheckurlService);
    expect(service).toBeTruthy();
  });
});
