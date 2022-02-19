<template>
  <div class="description_wrapper">
      <slot class="description_slot"></slot>
  </div>
</template>

<script>
export default {
    name: 'DescriptionLayout'
}
</script>

<style lang="scss">
.description_wrapper {
  box-shadow: 0 4px 16px 0 rgba(0, 0, 0, .27);
  width:95%;
  height: 20rem;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
  .description_slot{
    font-size:24px;
    margin-top:2rem;
    font-weight: bold;
    text-align: center;
  }
}
</style>