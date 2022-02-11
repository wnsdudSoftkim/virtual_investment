<template>
    <div>
        <div v-for="index in project" :key="index">
            <div class="project-container" @click="redirectProject">
                <div v-if="index.title !== '' ">
                    {{index.title}}
                </div>
                <div v-if="index.description !== '' ">
                    {{index.description}}
                </div>
                <div v-if="index.profit !== 0 ">
                    {{index.profit}}
                </div>
            </div>

        </div>
    </div>


</template>

<script>
import {computed} from 'vue'
import {useStore} from 'vuex'
export default {
    name:"chartLayout",
    data:()=> ({
        store:useStore(),
        project:{},
        query: {}

    }),
    mounted() {
        this.connect()
        console.log(this.project[0])
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
    flex-direction:column;
    margin:1rem;
    cursor:pointer;
    background:white;
    border-radius:4px;
    box-shadow:rgba(0, 0, 0, 0.18) 0px 4px 16px 0px;
    transition: box-shadow 0.25s ease-in 0s, transform 0.25s ease-in 0s;
    overflow:hidden;
    
    &:hover {
        transform: translateY(-8px);
        box-shadow: rgba(0, 0, 0, 0.28) 0px 12px 20px 0px;
    }
}

</style>