import {Body} from '@angular/http/src/body';
import {Injectable} from '@angular/core';
import {Response} from "@angular/http";

@Injectable()
export class ResponseService {

    parseData(response: Response): any {
        return response.json();
    }

    parseErrors(response: Response): Array<any> {
        if (response instanceof Response) {
            return response.json().errors;
        } else {
            return [response]
        }
    }

}