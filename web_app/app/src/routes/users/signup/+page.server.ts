import { fail } from '@sveltejs/kit';
import type { Actions } from './$types';
import { redirect } from '@sveltejs/kit';

export const actions = {
    default: async ({ cookies, request }) => {
        const data = await request.formData();
        const email = data.get('email');
        const login = data.get('login');
        const password = data.get('password');
    
        const response = await fetch('http://'+import.meta.env.SERVER_IP+':8080/user/signup', {
            method: 'POST',
            body: JSON.stringify({ "login": login, "email": email, "password": password }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.status == 200) {
            throw redirect(302, '/users/signin'); 
        }
        if (response.status == 400) {
            return fail(400, { is_user: false })
        }
    }
} satisfies Actions;    