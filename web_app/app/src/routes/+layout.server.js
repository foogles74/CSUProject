export async function load({ cookies }) {
	const auth = cookies.get('token');
    if (auth === undefined){
        return {
            auth: false
        };  
    }
    try {
        const response = await fetch('http://'+import.meta.env.SERVER_IP+':8080/user/validate', {
            method: 'POST',
            body: JSON.stringify({"token": auth}),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.status === 200) {
            return {
                auth: true
            };
        } else {
            return {
                auth: false
            };
        }
    }catch (e) {
        return {
                auth: false
            };
    }
}