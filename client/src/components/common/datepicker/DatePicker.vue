<script >
  import { ref } from 'vue';
  import Datepicker from 'vue3-date-time-picker';
  import 'vue3-date-time-picker/dist/main.css'
  export default {
    components: { Datepicker },
    setup() {
      const startDate = ref(new Date(2020, 1));
      const date = ref();
        return {
          date,
          startDate
      }
    },
    data() {
      return {
        year: [2017,2021]

      }
    }
  };
</script>

<template>
  <Datepicker v-model="date" class="pick_input" :yearRange="[2017, 2021]" :startDate="startDate"  :state="true" placeholder="Select Date" ></Datepicker>
</template>
<style lang="scss">
.pick_input{
    height: 30px;
    padding-left: 14px;
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
    font-family: "Open Sans", sans-serif;
}
</style>