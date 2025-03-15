document.addEventListener('DOMContentLoaded', function() {
    const estadoField = document.getElementById('id_estado');
    const municipioField = document.getElementById('id_municipio');
    const parroquiaField = document.getElementById('id_parroquia');

    if (estadoField && municipioField && parroquiaField) {
        // Función para cargar municipios basados en el estado seleccionado
        function cargarMunicipios() {
            const estadoId = estadoField.value;
            if (estadoId) {
                fetch(`/api/geo/municipios/${estadoId}/`)
                    .then(response => response.json())
                    .then(data => {
                        municipioField.innerHTML = '<option value="">---------</option>';
                        data.forEach(municipio => {
                            const option = document.createElement('option');
                            option.value = municipio.id;
                            option.textContent = municipio.descripcion;
                            municipioField.appendChild(option);
                        });
                    });
            } else {
                municipioField.innerHTML = '<option value="">---------</option>';
            }
        }

        // Función para cargar parroquias basados en el municipio seleccionado
        function cargarParroquias() {
            const municipioId = municipioField.value;
            if (municipioId) {
                fetch(`/api/geo/parroquias/${estadoId}/${municipioId}`)
                    .then(response => response.json())
                    .then(data => {
                        parroquiaField.innerHTML = '<option value="">---------</option>';
                        data.forEach(parroquia => {
                            const option = document.createElement('option');
                            option.value = parroquia.id;
                            option.textContent = parroquia.descripcion;
                            parroquiaField.appendChild(option);
                        });
                    });
            } else {
                parroquiaField.innerHTML = '<option value="">---------</option>';
            }
        }

        // Escucha cambios en el campo de estado
        estadoField.addEventListener('change', cargarMunicipios);

        // Escucha cambios en el campo de municipio
        municipioField.addEventListener('change', cargarParroquias);

        // Carga inicial de municipios y parroquias
        cargarMunicipios();
        cargarParroquias();
    }
});