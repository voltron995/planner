import {Component, Input,Output, OnInit, AfterContentInit} from '@angular/core';
import {FormBuilder, FormGroup,FormArray,FormControl} from '@angular/forms';
import {SelectModule} from 'angular2-select';
import {DishService} from "../../services/dish.service";
import {Dish} from "../../models/dish";
import {FileUploader} from "ng2-file-upload";
import {Router} from "@angular/router";
import {MessageService} from "../../../../../main/services/message.service";
import {ResponseError} from "../../../../../main/models/errors";
import {Ingredient} from "../../../ingredients/models/ingredients";
import {IngredientService} from "../../../ingredients/services/ingredients.service";

@Component({
    selector: 'dish-edit-form',
    templateUrl: 'dish-edit.form.html',
    styleUrls: [
        'dish-edit.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class DishEditForm {


    @Input()
    eventId: string;

    @Input()
    dish: Dish;

    uploader: FileUploader;
    imagePreview: string;

    form: FormGroup;

    myOptions : Array<any>=[];
    ingredients: Ingredient[];
    constructor(

        private fb: FormBuilder,
        private ingrSrv:IngredientService,
        private dishSrv: DishService,
        private router: Router,
        private msgSrv: MessageService,

    ) {

    }

    ngOnInit() : void {
      this.initIngrlist();
      this.initForm();
      this.initUploader();
    };


    initOptions(): void {
      let opts=new Array();
      for (let i of this.ingredients) {
        console.log(i)
          opts.push({
              value: i.id.toString(),
              label: i.name.toString()
          });
      }
      this.myOptions = opts
    };

    private initForm() {
  //     let ingredients:FormArray = new FormArray([]);
  //     for(let i=0;i<this.dish.ingredients.length; i++){
  //     ingredients.push(new FormGroup({
  //     name:new FormControl(this.dish.ingredients[i].name),
  //     quantity:new FormControl(this.dish.ingredients[i].name)
  //   }
  //
  //   )
  // )
  // }

        this.form = this.fb.group({
            name: [this.dish.name],
            description: [this.dish.description],
            img_path: [this.dish.image],
            ingredients:this.fb.array([this.initIngredients()]),
            event_id: this.eventId

        });
      }
      initIngredients(){
          return this.fb.group({
            name:[this.dish.ingredients],
            quantity:[this.dish.ingredients]
          })
        }
      addIngredient() {
         const control = <FormArray>this.form.controls['ingredients'];
         control.push(this.initIngredients());
     }



    initUploader() {
        let _this = this;
        let uploader = new FileUploader({
            url: '/api/v1.0/uploads/dish-images',
            autoUpload: true,
            removeAfterUpload: true
        });

        uploader.onCompleteItem = function (item: any, response: string, status: number) {
            var json = JSON.parse(response);
            this.imagePreview = json.link;
            this.form.patchValue({'img_path': json.id});
        };

        this.uploader = uploader;
        this.imagePreview = this.dish.imageLink;
    }


    onSubmit() {
        let values = this.form.value;

        // values.ingredients = [
        //      {
        //          "ingredient": {"id":4},
        //           "quantity":300
        //     }
        // ];

        this.dishSrv
            .put(this.dish.id, values)
            .then((dish: Dish) => {
                this.msgSrv.success(`Dish ${dish.name} successfully updated.`);
                this.router.navigate(['events', this.eventId])
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });

          }

    initIngrlist(): void {
        this.ingrSrv
            .list()
            .then(ingredients => {
              this.ingredients = ingredients;
              this.initOptions();
              console.log(ingredients, 'ingr');
            });
      }
  //   onSel(ingredient:Ingredient) {
  //     console.log(ingredient)
  //     this.selectedIngr = ingredient;
  //     // ... do other stuff here ...
  // }
    }
