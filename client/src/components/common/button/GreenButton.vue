<template>
  <button class="btn green-btn">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name:'green-button',
}
</script>

<style lang="scss">
.green-btn{
    background-color: #c2fbd7;
    border-radius: 50px;
    border-width: 0;
    box-shadow: rgba(25,25,25,.04) 0 0 1px 0,rgba(0,0,0,.1) 0 3px 4px 0;
    color: green;
    cursor: pointer;
    display: inline-block;
    font-family: Arial,sans-serif;
    font-size: 1em;
    height: 50px;
    padding: 0 25px;
    transition: all 200ms;
    &:hover {
        background-color: #afe6c3;
        transform: scale(1.01);
    }
}
</style>