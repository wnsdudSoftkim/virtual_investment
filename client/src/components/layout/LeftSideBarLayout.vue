<template>
    <div class="leftSideContainer">
        <span class="material-icons">
            home
        </span>
        <span class="material-icons">
            dashboard
        </span>
    </div>
  
</template>

<script>
export default {
    name:'LeftSideBarLayout'

}
</script>

<style lang="scss">
    .leftSideContainer {
        z-index: 1;
        position: sticky;
        flex-direction: column;
        height:100vh;
        top:0;
        justify-content: space-around;
        background-color: rgba(255, 255, 255, 1);
        box-sizing: inherit;
        width: 10%;

    }
</style>