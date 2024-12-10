<script>
    export let form;
    import {Section, Register} from "flowbite-svelte-blocks";
    import {Button, Checkbox, Label, Input, Alert} from "flowbite-svelte";
</script>

<Section name="blog">
    <div class="p-6 my-2 md:min-w-96 bg-slate-800 space-y-4 md:space-y-6 sm:p-8">
        <form class="flex flex-col space-y-6" method="POST">
            <h3 class="text-xl font-medium text-gray-900 dark:text-white p-0">Регистрация</h3>
            <Label class="space-y-2">
                <span>Логин:</span>
                <Input type="text" name="login" placeholder="логин" required/>
            </Label>
            <Label class="space-y-2">
                <span>Сумма:</span>
                <Input type="number" name="balance" placeholder="0" required/>
            </Label>
            <Button type="submit" class="w-full1 text-green-300">Пополнить</Button>
        </form>
    </div>
</Section>