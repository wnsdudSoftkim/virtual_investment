<template>
    <div class="leftSideContainer">
        <div class="icon-home">
            <router-link to='/'>
                <span class="material-icons icons icons-home">
                    home
                    
                </span>
            </router-link>
            <hr style="border: 1px solid gray">
        </div>
        <div class="icon-material">
            <span class="material-icons icons">
                dashboard
            </span>
            <div class="projectSection">
            </div>
        </div>
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
        
        background-color: rgba(255, 255, 255, 1);
        box-sizing: inherit;
        width: 10%;
        display: flex;
        padding:1rem;
        align-items: center;

    }
    .icons {
        color:$baseColor;
        font-size:48px

    }
    .icons-home {
        cursor:pointer;
        &:hover {
            transition: .8s;
            color:#000;
        }
    }
    .icon-home {
       
        flex:1rem;
    }
    .icon-material {
        flex:40rem;
    }    
</style>