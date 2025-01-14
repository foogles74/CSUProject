import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import { redirect } from '@sveltejs/kit';

export const actions = {
    default: async ({ cookies, request }) => {
        const data = await request.formData();
        const login = cookies.get('email');
        const balance = data.get('balance');
        const response = await fetch('http://'+process.env.SERVER_IP+':8080/balance/change_balance', {
            method: 'POST',
            body: JSON.stringify({ "login": login, "value": balance}),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.status == 200) {
            throw redirect(302, '/');
        }
    }
} satisfies Actions;