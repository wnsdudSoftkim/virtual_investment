<template>
    <div class="main-footer">
        <div class="left-footer">
            <span class="left-footer-span">
                    Left Footer
            </span>
        </div>
        <div class="right-footer">
            <span class="right-footer-span">
                Right Footer
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
        height: 2rem;
        border-top: 1px solid #eee;
        background: #fff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
    }
    .left-footer{
        .left-footer-span{
            color:$baseColor;
        }
    }
    .right-footer{
        .right-footer-span{
            color:$baseColor;
        }
    }
</style>