export class ResponseError {
    code: number;
    detail: string;
    source: string;
    title: string;

    constructor(attrs: any) {
        this.code = attrs.code;
        this.detail = attrs.detail;
        this.source = attrs.source;
        this.title = attrs.title;
    }

    public static newFromResponse(response: any): ResponseError {
        return new this({
            code: response.code,
            detail: response.detail || 'Oops! An error occurred.',
            source: response.source,
            title: response.title
        });
    }
}