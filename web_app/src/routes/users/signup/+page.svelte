<script lang="ts">
    /**  @type {import('./$types').ActionData} */
export let form;
import { Section, Register } from "flowbite-svelte-blocks";
import { Button, Checkbox, Label, Input, Alert } from "flowbite-svelte";
</script>

<Section name="login">
    <div class="p-6 my-2 md:min-w-96 bg-slate-800 space-y-4 md:space-y-6 sm:p-8">
      <form class="flex flex-col space-y-6" method="POST"> 
        <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Регистрация</h3>
        <Label class="space-y-2">
          <span>Почта:</span>
          <Input type="email" name="email" placeholder="name@company.com" required />
        </Label>
        <Label class="space-y-2">
            <span>Логин:</span>
            <Input type="text" name="login" placeholder="login" required />
          </Label>
        <Label class="space-y-2">   
          <span>Пароль:</span>    
          <Input type="password" name="password" placeholder="•••••" required />
        </Label>
        {#if form?.is_user == false}
        <Alert border color="red">
            <span slot="icon"><svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"></path></svg>
            </span>
            <span class="font-medium">Пользователь существует!</span>
        </Alert>
        {/if}

        <Button type="submit" class="w-full1 text-green-300">Sign up</Button>  
      </form>
    </div>

</Section>