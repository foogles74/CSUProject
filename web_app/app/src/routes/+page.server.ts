import type {Actions} from './$types';
import type {PageServerLoad} from './$types';
import {redirect} from "@sveltejs/kit";
import {goto} from "$app/navigation";


export const load: PageServerLoad = async ({data,cookies }) => {
    const email = cookies.get('email');
    try {
        // @ts-ignore
        const response = await fetch('http://' + process.env.SERVER_IP + ':8080/get_chat_history', {
            method: 'POST',
            body: JSON.stringify({"user": email, "chat_name": "Первый Чат"}),
            headers: {
                'Content-Type': 'application/json',
                    'x-sveltekit-action': 'true'
            }
        });
        if (response.status === 200) {
            const history = await response.json()
            let test: string[] = []
            history.forEach(function (element) {
                // console.log(element);
                test.push(element)
            })

            return {"messages": test}
        } else {

        }
    } catch (e) {
        console.log(e)
    }
};

export const actions = {
    default: async ({cookies, request}) => {
        // console.log("start")
        try {
            const email = cookies.get('email');
            const data = await request.formData();
            // @ts-ignore
            if (data.get("message").length > 1){
            const response = await fetch('http://' + process.env.SERVER_IP + ':8080/request_model', {
                method: 'POST',
                body: JSON.stringify({"text": data.get("message"), "user": email, "chat_name": data.get("chat_name")}),
                headers: {
                    'Content-Type': 'application/json',
                    'x-sveltekit-action': 'true'
                }
            });
            // console.log("end")
            if (response.status === 200) {
                const text = await response.json()
                // console.log(text.bot)
                return {otvet: text.bot, vopros: data.get("message")}
            }
            }
        } catch (e) {
            console.log(e)
        }
    }
} satisfies Actions;