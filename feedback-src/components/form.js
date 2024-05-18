import Vue from '../lib/vue.js';

import { UsersService } from '../services/usersService.js';

let Fform = Vue.component('fform', {
  	template:
			'<div class="feedback-form">'+
        '<div class="feedback-form__inputs">'+
          '<div class="feedback-input"><span>Name:</span><input type="text" v-model="name" class="feedback-form__inputs-from"></input></div>'+
          '<div class="feedback-input"><span>Email:</span><input type="email" v-model="email" class="feedback-form__inputs-email"></input></div>'+
          '<div class="feedback-input"><span>Phone:</span><input type="phone" v-model="phone" class="feedback-form__inputs-phone"></input></div>'+
          '<div class="feedback-input"><span>Comment:</span><textarea v-model="comment" class="feedback-form__inputs-comment"></textarea></div>'+
          '<div class="feedback-input"><input type="submit" @click="validateForm" class="feedback-form__inputs-submit" value="Submit"></input></div>'+
        '</div>'+
        '<div class="feedback-form__message">{{message}}</div>'+
      '</div>',
    data: function () {
        return {
          email: "",
          phone: "",
          comment: "", 
          name: "",
          message: ""
        }
    },
    created: function() {
      this.comments = this.param;
    },
    methods: {
      validateForm: function(){
        let self = this;

        let user = {
          email: this.email,
          phone: this.phone,
          comment: this.comment,
          name: this.name
        };
        UsersService.checkpost(function(data) {
          self.message = data.key;     
          
          if (data.status == "ok"){
	          self.$root.$emit("addedComment", {comment: user});
          }
        }, user)
      },
      reload: function(){
        location.reload();
      }
    }
})

export { Fform };
