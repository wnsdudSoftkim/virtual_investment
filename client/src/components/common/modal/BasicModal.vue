<template>
<div class="modal_container" id="app">
  <div class="add-product" :class="{'open': formOpen}">
    <div class="button-copy" v-show="!formOpen" @click="formOpen = true" style="font-size:18px">버튼을 눌러 프로젝트를 생성해보세요!</div>
    <form>

      <div class="form--field">
        <label>프로젝트 이름</label>
        <input type="text" class="form--element" name="title" v-model="productData.title" placeholder="Title" required="">
      </div>
      <div class="form--container -inline">
        <div class="form--field -short">
          <label>시작 날짜 *</label>
          <date-picker v-model="pickedDate"></date-picker>
        </div>
        <div class="form--field -short">
          <label>투자 종목 *</label>
          
          <select v-model="productData.symbol" class="form--element">
              <option value="BTC">BTC</option>
              <option value="A">A</option>
              <option value="B">B</option>
              <option value="C">C</option>
          </select>
        </div>
        <div class="form--field -short">
          <label>투자 금액 *</label>
          <span class="form--price">$</span>
          <input type="text" class="form--element" name="list_price" v-model="productData.price" placeholder="Price" required="" min="0" max="500" pattern="\d+(\.\d{2})?">
        </div>
      </div>
      <!-- <div class="form--field">
        <label class="emoji">
          Is Featured
          <input type="checkbox" name="is_featured" v-bind="productData.is_featured">
          <span></span>
        </label>
        <p class="featured-note">If Is Featured is selected the product will appear in a large card.</p>
      </div> -->
      <div class="form--field">
        <label></label>
        <textarea class="form--element textarea" v-model="productData.description" placeholder="자유롭게 설명해보세요">                                
        </textarea>
      </div>

      <button type="submit" class="submit-button" @click.stop.prevent="submitForm" >Add Product</button>
      <div class="cancel"><span @click="cancel()">Cancel</span></div>
    </form>
  </div>
</div>
</template>

<script>
import { ref } from 'vue'
import {useStore} from 'vuex'
import DatePicker from '@/components/common/datepicker/DatePicker'
export default {
    name:'BasicModal',
    components: {DatePicker},
    computed: {
      PAYLOAD() {
        return this.productData
      },
      QUERY(){
        return {
          'price':this.productData.price,
          'date': this.pickedDate.toISOString(),
          'symbol':this.productData.symbol
        }
      },
      QUANTITY() {
        return this.store.getters.getquantity
      }
    },
    data: ()=> ({
        formOpen:false,
        store:useStore(),
        productData: {
            title: '',
            rating: '',
            price: '',
            symbol: 'BTC',
            pickedDate:'',
            quantity:0
        },
        pickedDate: ref(new Date()),
        symbolList: ['BTC', "ETR", "AAA", "BBB", "CCC"]
    }),
    methods: {
        resetForm() {
            this.productData = {
                title: '',
                rating: '',
                price: '',
                list_price: '',
        
            }
        },
        storeProject(value) {
          this.store.dispatch('updateProject', value)
        },
        storeQuery(value) {
          this.store.dispatch('updateQuery', value)
        },
        cancel() {
            this.formOpen = false
            this.resetForm()
        },
        submitForm() {
          let project = {
            title:this.productData.title,
            description: this.productData.description,
            profit:0,
            quantity: this.productData.quantity
          }
          this.storeProject(project)
          this.storeQuery(this.QUERY)
          this.$router.push({path: '/chart', query:this.QUERY})
        },
    }

}
</script>

<style lang="scss">
.modal_container {
  // background-image: linear-gradient(-128deg, rgba(36, 32, 255, 0.93) 3%, rgba(241, 28, 224, 0.93) 88%, rgba(229, 29, 236, 0.93) 100%);
  display: flex;
  width: 100%;
  height: 20%;
  justify-content: center;
  align-items: center;
  box-shadow:rgba(0, 0, 0, 0.18) 0px 4px 16px 0px;
  z-index: 10;
}

.add-product {
  &.open {  
    background-color: #fafafa75;

    padding: 18px 32px;
    border-radius: 5px;
    width: 420px;
    height: 398px;
    cursor: default;
    form {
      opacity: 1;
      transition: opacity 0.1s ease;
      transition-delay: 0.3s;
      height: auto;
    }
  }
  transition: all 0.3s ease;
  background-color: $baseColor;
  height: 144px;
  width: 100%;
  box-shadow: 0 4px 16px 0 rgba(0, 0, 0, .27);
  cursor: pointer;
  .button-copy {
    text-align: center;
    line-height: 144px;
    text-transform: uppercase;
    font-weight: bold;
    color: #f7f7f7;
  }
  form {
    transition: none;
    opacity: 0;
    height: 0;
    overflow: hidden;
  }
  .cancel {
    font-size: 12px;
    text-align: center;
    margin-top: 1em; 
    span {
      cursor: pointer;
      &:hover {
        text-decoration: underline;
      }
    }
  }
}

.submit-button {
  display: block;
  background-color: #3498DB;
  height: 40px;
  border-radius: 20px;
  line-height: 36px;
  text-align: center;
  color: #fff;
  text-transform: uppercase;
  font-size: 0.875em;
  border: none;
  font-weight: 700;
  padding: 0 34px;
  margin: 30px auto;
  img {
    position: relative;
    top: 3px;
    right: 6px;
  }
  &:hover {
    background-color: darken(#3498DB, 10%);
    cursor: pointer;
  }
}

.featured-note {
  color: #949494;
  font-size: 12px;
  margin: 4px 0px;
  line-height: 18px;
  font-style: italic;
}

form * {
  outline: none;
}

label {
  display: block;
  font-size: 14px;
  font-weight: bold;
  user-select: none;
  &.emoji {
    input {
      -webkit-appearance: none;
      -moz-appearance: none;
      appearance: none;
      height: 21px;
      margin: 0;
      display: none;
      &+span:after {
        content: "😶";
        font-size: 18px;
        top: 2px;
        left: 2px;
        position: relative;
        height: 18px;
        display: inline-block;
      }
      &:checked+span:after {
        content: "😀";
      }
    }
  }
}

.form--field {
  width: 420px;
  margin: 10px 0;
  &.-short {
    width: 120px;
  }
}

.form--price {
  position: absolute;
  line-height: 38px;
  width: 16px;
  color: #C7C7C7;
  text-align: center;
  & + input {
    padding-left: 14px;
  }
}

.form--container {
  width: 420px;
  &.-inline {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-bottom: -12px;
  }
}

.form--element {
  background-color: #fff;
  border: 1px solid #ECECEC;
  border-radius: 3px;
  font-size: 14px;
  line-height: 28px;
  padding: 0 4px;
  color: #3D3D3D;
  width: 100%;
  margin: 4px 0;
  box-sizing: border-box;
  font-family: 'Open Sans', sans-serif;
  &:focus {
    border: 1px solid #FFC145;
    border-radius: 2px;
  }
  &:not(.texteare) {
    height: 30px;
  }
  &.textarea {
    height: 80px;
    resize: none;
  }
}

a {
  text-decoration: none;
  cursor: pointer;
}

::selection {
  background-color: #F5617A;
  color: #fff;
}

::-moz-selection {
  background-color: #F5617A;
  color: #fff;
}
</style>