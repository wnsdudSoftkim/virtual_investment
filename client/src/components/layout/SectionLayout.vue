<template>
    <div class="section-layout" >
        <div class="section-container">
            <slot></slot> <!--여기에 넣을 것 !-->
        </div>
    </div>
</template>

<script>
export default {
    name:"section-layout",


}
</script>

<style lang="scss">
.section-layout{
    padding:2rem;
    padding-left:12rem;
    padding-right:12rem;
    .section-container{
        width:100%;
        height:40rem;
        background: $secondColor;
    }
}
</style>