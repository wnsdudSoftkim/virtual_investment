<template>
  <button class="button-48" role="button" @click="changeButtonValue"><span class="text">{{this.button_value}}</span></button>
</template>

<script>

import {useStore} from 'vuex'
import Swal from 'sweetalert2'
import {computed} from 'vue'

export default {
    
    name:'SellButton',
    data: ()=> ({
        button_value: "Sell",
        store: useStore(),
        count: 0,
        symbol:''
    }),
    mounted() {
      this.count= computed(() => this.store.getters.getquantity)
      this.symbol = computed(() => this.state.getters.getsymbol)
    },
    methods: {
        changeButtonValue() {
          if (this.count === 0) {
            this.alertTransactions()
          } else {
            this.descQuantity(this.count)
            this.getTransactions(this.count)
          }
          // SellAlert()
            // let message = this.store.getters.updatelastdate

            // if (this.button_flag === true) {
            //   methods.sendMessage(1)
            // }else {
            //   methods.sendMessage(message)
            // }
           
        },
        getTransactions(count) {
          //...
          Swal.fire(`1 ${this.symbol}를 매도합니다. 현재 보유량: ${count}`)
        },
        alertTransactions() {
          Swal.fire(`매도할 수량이 없습니다.`)
        }, 
        descQuantity(item) {
            this.store.dispatch('descQuantity', item)
        },
    } 
}
</script>

<style lang="scss">
.button-48 {
  align-items: center;
  border: 0;
  border-radius: 8px;
  box-sizing: border-box;
  color: white;
  display: flex;
  font-family: Phantomsans, sans-serif;
  font-size: 20px;
  justify-content: center;
  line-height: 1em;
  max-width: 100%;
  min-width: 140px;
  padding: 3px;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  cursor: pointer;
}


.button-48:hover {
  outline: 0;

}

.button-48 span {
  background-color: blue;
  padding: 16px 24px;
  border-radius: 6px;
  width: 100%;
  height: 100%;
  transition: 300ms;
  display: flex;
  align-items: center;
  justify-content: center;
}



@media (min-width: 768px) {
  .button-48 {
    font-size: 24px;
    min-width: 196px;
  }
}
</style>