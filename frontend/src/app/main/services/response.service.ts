import {Injectable} from '@angular/core';
import {Response} from "@angular/http";
import {ResponseError} from "../models/errors";

@Injectable()
export class ResponseService {

    parseData(response: Response): any {
        return response.json();
    }

    parseErrors(response: Response): ResponseError[] {
        try {
            return response
                .json()
                .errors
                .map((error: any) => ResponseError.newFromResponse(error));
        }
        catch (e) {
            return [
                new ResponseError({
                    code: 500,
                    detail: 'Server returned unexpected response.',
                    title: 'Something wrong.',
                })
            ];
        }
    }

}