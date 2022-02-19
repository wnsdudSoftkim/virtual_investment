<template>
    <div>
        <div v-for="index in project" :key="index">
            <div class="project-container" @click="redirectProject" v-if="index.title !=='SAMPLE' "  >
                <div class="flex-left">
                    <div class="project-title index" v-if="index.title !== 'SAMPLE' ">
                        <span class="bold">프로젝트</span>
                        <p>{{index.title}}</p>
                    </div>
                    <div class="project-profit index " v-if="index.profit !== 0 ">
                        <span class="bold">수익률</span>
                        <p>{{index.profit}}%</p>
                    </div>
                    <div class="project-description index" v-if="index.description !== 'SAMPLE' ">
                        <span class="bold">간단 설명</span>
                        <p>{{index.description}}</p>
                    </div>
                </div>
                <div class="lottie">
                    <lottie-player></lottie-player>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
import {computed} from 'vue'
import {useStore} from 'vuex'
import LottiePlayer from '@/components/common/lottie/LottiePlayer'
export default {
    name:"chartLayout",
    data:()=> ({
        store:useStore(),
        project:{},
        query: {}

    }),
    components: { LottiePlayer },
    mounted() {
        this.connect()
    },
    methods: {
        connect() {
            this.project = computed(() => this.store.getters.updateproject)
            this.query = computed(() => this.store.getters.updatequery)

        },
        redirectProject() {
            this.$router.push({path: '/chart', query:this.query})
        },
    }
}
</script>

<style lang="scss">
.project-container {
    display:flex;
    flex-direction:row;
    margin:2rem 0;
    padding: 1rem;
    border-radius: .5rem;
    justify-content: space-between;
    cursor:pointer;
    background:white;
    border-radius:4px;
    box-shadow:rgba(0, 0, 0, 0.18) 0px 4px 16px 0px;
    transition: box-shadow 0.25s ease-in 0s, transform 0.25s ease-in 0s;
    overflow:hidden;
    .flex-left {
        display: flex;
        
    }
    &:hover {
        transform: translateY(-4px);
        box-shadow: rgba(0, 0, 0, 0.28) 0px 12px 20px 0px;
    }
    .bold {
        font-size: 18px;
        color:$black;
        font-weight: bold;
    }
    .index {
        margin:0 2rem;
    }
}

</style>