<script>
    import { goto } from '$app/navigation';
    import { browser } from '$app/environment';

    export let form;

    if (browser && form?.success) {
        sessionStorage.removeItem('access_token');
        goto('/login');
    }
</script>