<template>
    <div class="main-footer">
        <div class="left-footer">
            <span class="left-footer-span">
                    ascasc
            </span>
        </div>
        <div class="right-footer">
            <span class="right-footer-span">

            </span>
        </div>
    </div>
</template>

<script>
export default {
    name:'main-footer'
}
</script>

<style lang="scss">
    .main-footer{
        position: fixed;
        z-index: 100;
        bottom: 0;
        width: 100%;
        height: 59px;
        border-top: 1px solid #eee;
        background: #fff;
    }
    .left-footer{
        .left-footer-span{
            color:$baseColor;
        }
    }
</style>