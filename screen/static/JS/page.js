document.addEventListener('DOMContentLoaded', function() {

    // ============= FUNCIONALIDAD MOSTRAR EL AÑO ACTUAL EN EL FOOTER ============
        document.getElementById('year').innerText = new Date().getFullYear();
    // =========== FIN FUNCIONALIDAD MOSTRAR EL AÑO ACTUAL EN EL FOOTER ==========

    // ================ FUNCIONALIDAD PARA ABRIR Y CERRAR EL MENU ================
        // Agregar event listener al botón de alternancia de menú
        document.querySelector('.menu_toggle').addEventListener('click', function() {
            this.classList.toggle('active');
            document.querySelector('.menu_container').classList.toggle('menu_container_move');
        });

    // Agregar event listener al documento para cerrar el menú al hacer clic fuera de él
        document.addEventListener('click', function(event) {
            var menuContainer = document.querySelector('.menu_container');
            var menuToggle = document.querySelector('.menu_toggle');

            // Verificar si el clic no ocurrió dentro de .menu_container o .menu_toggle
            if (!menuContainer.contains(event.target) && !menuToggle.contains(event.target)) {
                // Quitar la clase 'menu_container_move' si está presente
                menuContainer.classList.remove('menu_container_move');
                // Quitar la clase 'active' del botón de alternancia de menú si está presente
                menuToggle.classList.remove('active');
            }
        });
    // ============== FIN FUNCIONALIDAD PARA ABRIR Y CERRAR EL MENU ==============

});