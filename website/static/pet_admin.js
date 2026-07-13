document.addEventListener("DOMContentLoaded", function () {
    const status = document.getElementById("id_status");

    const rows = [
        document.querySelector(".field-new_owner"),
        document.querySelector(".field-phone"),
        document.querySelector(".field-mail"),
        document.querySelector(".field-taken_date"),
    ];

    function updateVisibility() {
        const show =
            status.value === "adopted" ||
            status.value === "foster";

        rows.forEach(row => {
            if (row) {
                row.style.display = show ? "" : "none";
            }
        });
    }

    updateVisibility();
    status.addEventListener("change", updateVisibility);
});