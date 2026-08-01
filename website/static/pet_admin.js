document.addEventListener("DOMContentLoaded", function () {
    const status = document.getElementById("id_status");

    const ownerRows = [
        document.querySelector(".field-new_owner"),
        document.querySelector(".field-phone"),
        document.querySelector(".field-mail"),
        document.querySelector(".field-taken_date"),
    ];

    const treatmentRows = [
        document.querySelector(".field-treatment_description"),
    ];

    function updateVisibility() {
        const showOwner =
            status.value === "adopted" ||
            status.value === "foster";

        const showTreatment =
            status.value === "treatment";

        ownerRows.forEach(row => {
            if (row) {
                row.style.display = showOwner ? "" : "none";
            }
        });

        treatmentRows.forEach(row => {
            if (row) {
                row.style.display = showTreatment ? "" : "none";
            }
        });
    }

    updateVisibility();
    status.addEventListener("change", updateVisibility);
});
