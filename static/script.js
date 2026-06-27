// Toggle a dropdown panel (Topics / About) and close any other open one.
function togglePanel(id) {
    const target = document.getElementById(id);
    document.querySelectorAll('.panel').forEach(function (p) {
        if (p !== target) p.classList.remove('show');
    });
    target.classList.toggle('show');
}

// Close panels when clicking outside the navbar.
document.addEventListener('click', function (event) {
    if (!event.target.closest('.navbar')) {
        document.querySelectorAll('.panel').forEach(function (p) {
            p.classList.remove('show');
        });
    }
});
