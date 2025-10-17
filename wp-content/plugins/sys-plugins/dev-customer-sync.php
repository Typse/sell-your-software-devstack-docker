<?php
/**
 * Plugin Name: Dev Customer Sync
 * Description: Simple plugin that exposes a shortcode [dev_customer_form] with a prefilled test form that posts to /api/customers.
 * Version: 0.1
 * Author: Dev
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

function dev_customer_form_shortcode($atts = []) {
    // default template values for quick testing
    $defaults = [
        'name' => 'Max Mustermann',
        'age' => '30',
        'email' => 'max@example.com',
        'country' => 'DE',
        'post_code' => '10115',
        'town' => 'Berlin',
        'street' => 'Hauptstr',
        'street_nr' => '1',
        'currency' => 'EUR',
    ];

    $id = 'dev-customer-form-' . wp_rand(1000, 9999);

    ob_start();
    ?>
    <form id="<?php echo esc_attr($id); ?>" class="dev-customer-form" style="max-width:600px">
        <h3>Dev Customer Form (test)</h3>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
            <input name="name" placeholder="Name" value="<?php echo esc_attr($defaults['name']); ?>" />
            <input name="age" type="number" placeholder="Age" value="<?php echo esc_attr($defaults['age']); ?>" />
            <input name="email" type="email" placeholder="Email" value="<?php echo esc_attr($defaults['email']); ?>" />
            <input name="country" placeholder="Country" value="<?php echo esc_attr($defaults['country']); ?>" />
            <input name="post_code" type="number" placeholder="Post Code" value="<?php echo esc_attr($defaults['post_code']); ?>" />
            <input name="town" placeholder="Town" value="<?php echo esc_attr($defaults['town']); ?>" />
            <input name="street" placeholder="Street" value="<?php echo esc_attr($defaults['street']); ?>" />
            <input name="street_nr" type="number" placeholder="Street Nr" value="<?php echo esc_attr($defaults['street_nr']); ?>" />
            <input name="currency" placeholder="Currency" value="<?php echo esc_attr($defaults['currency']); ?>" />
        </div>

        <div style="margin-top:12px">
            <button type="submit">Send to API</button>
            <span class="dev-customer-result" style="margin-left:12px"></span>
        </div>
    </form>
    <script>
    (function(){
        const form = document.getElementById('<?php echo esc_js($id); ?>');
        if (!form) return;
        form.addEventListener('submit', async function(e){
            e.preventDefault();
            const data = {};
            new FormData(form).forEach((v,k) => data[k]= v);

            const resultEl = form.querySelector('.dev-customer-result');
            resultEl.textContent = 'Sending...';

            try {
                const resp = await fetch('/api/customers', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data),
                    credentials: 'same-origin'
                });
                const json = await resp.json();
                if (resp.ok) {
                    resultEl.textContent = 'OK — ' + (json.email || 'created');
                } else {
                    resultEl.textContent = 'Error: ' + (json.detail || JSON.stringify(json));
                }
            } catch (err) {
                resultEl.textContent = 'Network error: ' + err.message;
            }
        });
    })();
    </script>
    <?php
    return ob_get_clean();
}
add_shortcode('dev_customer_form', 'dev_customer_form_shortcode');

// Small helper: show admin notice if plugin activated but WP_HOME mismatch
function dev_customer_sync_admin_notice() {
    if (!current_user_can('manage_options')) return;
    ?>
    <div class="notice notice-info is-dismissible">
        <p>Dev Customer Sync plugin active. Use the shortcode <code>[dev_customer_form]</code> on any page to test sending customers to <code>/api/customers</code>.</p>
    </div>
    <?php
}
add_action('admin_notices', 'dev_customer_sync_admin_notice');
