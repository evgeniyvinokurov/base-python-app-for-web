import Vue from '../lib/vue.js';

let Comments = Vue.component('comments', {
  	template:
      '<div class="comments">'+
          '<p class="comments__title">Comments already made:</p>'+        
          '<div class="comments__item" v-for="c in comments"><span>{{c["name"]}}</span>: <span>{{c["comment"]}}</span></div>'+
      '</div>',
    data: function () {
        return {
          comments: []
        }
    },
    props: ['data'],
    created: function() {
        let self = this;
        this.comments = this.data;

        this.$root.$on("addedComment", function(data){
            self.comments.push(data.comment)
        });
    }
})

export { Comments };
