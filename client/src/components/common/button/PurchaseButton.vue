<template>
    <button class="button-32" role="button" @click="changeButtonValue"><span class="text">{{this.button_value}}</span></button>
  
</template>

<script>
// import methods from '@/assets/js/common.js'
import {useStore} from 'vuex'
import Swal from 'sweetalert2'
import {computed} from 'vue'

export default {
    
    name:'PurchaseButton',
    data: ()=> ({
        button_flag: false,
        button_value: "BUY",
        store: useStore(),
        count: 0,
        price: 0

    }),
    props: {
        PROPS:String
    },
    mounted() {
      this.count = computed(() => this.store.getters.getquantity)
      this.price = computed(() => this.store.getters.getPriceAsset)
    },
    methods: {
        changeButtonValue() {
          this.increaseInvestAsset(this.price)
          this.ascQuantity(this.count)
          this.getTransactions(this.count)     
        },
        getTransactions(count) {
          //...
          Swal.fire(`1 ${this.PROPS}를 구매하셨습니다. 현재 구매량 : ${count}`)
        }, 
        ascQuantity(item) {
            this.store.dispatch('ascQuantity', item)
        },
        receiveProps() {
          this.symbol = this.PROPS
        },
        increaseInvestAsset(item) {
          this.store.dispatch('IncreaseAsset', item)
        }
    }, 
    watch: {
      'PROPS': 'receiveProps'
    }
}
</script>

<style lang="scss">
.button-32 {
  align-items: center;
  border: 0;
  border-radius: 8px;
  box-sizing: border-box;
  color: black;
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
.button-32:hover {
  outline: 0;

}

.button-32 span {
  background-color:  rgba(255, 255, 255, 0.308);
  box-shadow: 0 4px 16px 0 rgba(0, 0, 0, .22);

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
  .button-32 {
    font-size: 24px;
    min-width: 196px;
  }
}
</style>