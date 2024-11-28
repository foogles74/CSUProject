<script>
    import "../app.css";
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger  } from 'flowbite-svelte';
    let { data } = $props(); 
</script>   
<div class="basa overflow-hidden">
    <Navbar>
        <NavBrand href="/">
          <img src="../src/images/cat.png" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
          <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">CatChat</span>
        </NavBrand>
        <NavHamburger  />
        <NavUl >
          <NavLi href="/">Чатик</NavLi>
          <NavLi href="https://github.com/foogles74">О нас</NavLi>
          {#if data.auth === false}
            <NavLi href="/users/signin">Авторизация</NavLi>
          {/if}
          {#if data.auth === true}
            <NavLi href="/users/signin">Пополнить баланс</NavLi>
            <NavLi href="/users/logout" data-sveltekit-reload>Выйти</NavLi>
          {/if}
        </NavUl>
      </Navbar>
      
	<div class="slot">
		<slot />
	</div>
</div >
<style>
    :global(body) {
        background-color: #a5a199;
        color: #ffffff;
        transition: background-color 0.3s
    }
    .basa {
		height: 100%;
		display: flex;
		justify-content: flex-start;
		flex-direction: column;
		width: 100%;
		min-height: 100vh;
	}
	.slot {
		height: 100%;
	}

</style>