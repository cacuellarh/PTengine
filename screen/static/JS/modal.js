document.addEventListener('DOMContentLoaded', function() {

    // ====================== MODAL DE REGISTRO DE PRODUCTO ======================
        const confirmModalPrice = document.getElementById('confirm_modalprice');
        if (confirmModalPrice !== null) {
            confirmModalPrice.addEventListener('click', function() {
                var productForm = document.getElementById('product_form');
                if (productForm !== null) {
                    productForm.classList.remove('disabled');
                }
            });
        }
        const closeProductForm = document.getElementById('close_product_form');
        if (closeProductForm !== null) {
            closeProductForm.addEventListener('click', function() {
                var productForm = document.getElementById('product_form');
                if (productForm !== null) {
                    productForm.classList.add('disabled');
                }
            });
        }
    // ==================== FIN MODAL DE REGISTRO DE PRODUCTO ====================

    // ========================= MODAL AYÚDANOS A MEJORAR ========================
        const openModalForm = document.getElementById('open_modal_form');
        if (openModalForm !== null) {
            openModalForm.addEventListener('click', function() {
                var helpUsForm = document.getElementById('help_us_form');
                if (helpUsForm !== null) {
                    helpUsForm.classList.remove('disabled');
                }
            });
        }
        const closeHelpUsForm = document.getElementById('close_help_us_form');
        if (closeHelpUsForm !== null) {
            closeHelpUsForm.addEventListener('click', function() {
                var helpUsForm = document.getElementById('help_us_form');
                if (helpUsForm !== null) {
                    helpUsForm.classList.add('disabled');
                }
            });
        }
    // ====================== FIN MODAL AYÚDANOS A MEJORAR =======================

});