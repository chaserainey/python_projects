document.addEventListener('DOMContentLoaded', function () {
    var dropdown = document.querySelector('.dropdown');
    var dropdownContent = document.querySelector('.dropdown-content');

    dropdown.addEventListener('mouseover', function () {
        dropdownContent.computedStyleMap.display = 'block';
    });

    dropdown.addEventListener('mouseout', function () {
        dropdownContent.computedStyleMap.display = 'none';
    });
});