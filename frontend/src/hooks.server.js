import { redirect } from '@sveltejs/kit';

export async function handle({ event, resolve }) {

    const sessionCookie = event.cookies.get('session');
    const protectedRoutes = ['/dashboard'];
    const currentPathName = event.url.pathname;

    if (protectedRoutes.some(path => currentPathName.startsWith(path)) && !sessionCookie) {
        throw redirect(303, '/login');
    }

    return await resolve(event);
}
