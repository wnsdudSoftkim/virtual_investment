<template>
    <div class="main-footer">
        <div class="left-footer">
            <span class="left-footer-span bold">
                <a href="https://objective-blackwell-219591.netlify.app/" target="_blank" style="color:black;">Blog</a>
            </span>
            <span class="left-footer-span bold">
                <a href="https://github.com/wnsdudSoftkim/virtual_investment" target="_blank" style="color:black;">Github</a>
            </span>
            <!-- <span class="left-footer-span bold">
                <a href="https://github.com/wnsdudSoftkim/virtual_investment" target="_blank" style="color:black;">c</a>
            </span> -->
        </div>
        <div class="right-footer">
            <span class="right-footer-span">
                <div class="first_met bold" v-if="this.cbvalue === 0">
                    처음뵙네요! 수익모델을 만들어보세요
                </div>
                <div class="profit_overview" v-if="this.cbvalue !== 0">
                    <div class="profit_good bold" v-if="this.cbvalue < 0">
                        <b>{{this.cbvalue}}%</b> 최근 수익이 아쉽네요 다시 한번 시도해보세요
                    </div>
                    <div class="profit_good bold" v-if="this.cbvalue > 0">
                        <b>{{this.cbvalue}}%</b> 최근 수익이 높네요! 잘 하고 있습니다!
                    </div>
                </div>
            </span>
        </div>
    </div>
</template>

<script>
export default {
    name:'main-footer',
    props: {
        cbvalue: Number
    },
    methods: {
        showLastProfit() {
            // console.log(this.cbvalue)
        }
    },
    mounted() {
        this.showLastProfit()
    },
    watch: {
        // cbvalue: function() {
        //     console.log(this.cbvalue)
            
        // }
        'cbvalue': 'showLastProfit'
    }
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
        justify-content: space-around;
        align-items: center;
        padding: 1rem;
    }
    .left-footer{
        display:flex;
        margin-right: .5rem;
        .left-footer-span{
            color:$baseColor;
            a {
                padding:2rem;
                &:hover{
                    color: hsla(0,0%,100%,.9);
                }
            }
        }
    }
    .right-footer{
        .right-footer-span{
            color:$baseColor;
        }
    }
    .bold {
        font-size:18px;
        color:#000;

    }
</style>