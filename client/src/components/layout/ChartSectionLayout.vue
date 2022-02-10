<template>
    <div>
        <div v-for="index in project" :key="index">
            <div class="project-container">
                <div>{{index.title}}</div>
                <div>{{index.description}}</div>
                <div>{{index.profit}}</div>
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
        project:{}

    }),
    mounted() {
        this.connect()
        console.log(this.project[0])
    },
    methods: {
        connect() {
           this.project= computed(() => this.store.getters.updateproject)

        },
    }
}
</script>

<style lang="scss">
.project-container {
    display:flex;
    padding: 1rem;
}

</style>