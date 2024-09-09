// Функція для валідації номера телефону
function validatePhoneNumber(phone) {
    const phonePattern = /^\+?\d{10,12}$/;
    return phonePattern.test(phone);
}

// Функція для валідації імені та прізвища (два слова)
function validateFullName(name) {
    const words = name.trim().split(/\s+/);  // Розділяє по пробілах
    return words.length === 2;  // Повертає true, якщо введено рівно 2 слова
}

// Функція для перевірки перед відправкою форми
function validateForm(event) {
    const nameInput = document.getElementById('name');
    const phoneInput = document.getElementById('phone');

    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();

    let isValid = true;

    // Очистити всі помилки та повернути поля до нормального стану
    nameInput.style.borderColor = '';
    nameInput.style.backgroundColor = '';
    phoneInput.style.borderColor = '';
    phoneInput.style.backgroundColor = '';

    // Перевірка імені та прізвища
    if (!validateFullName(name)) {
        nameInput.style.borderColor = 'red';  // Підсвітити поле червоним
        nameInput.style.backgroundColor = '#ffcccc';  // Зробити фон червоним
        isValid = false;
    }

    // Перевірка номера телефону
    if (!validatePhoneNumber(phone)) {
        phoneInput.style.borderColor = 'red';  // Підсвітити поле червоним
        phoneInput.style.backgroundColor = '#ffcccc';  // Зробити фон червоним
        isValid = false;
    }

    // Якщо форма не валідна, зупиняємо відправку
    if (!isValid) {
        event.preventDefault();
    }
}

// Додаємо обробник події до форми
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('registrationForm');
    form.addEventListener('submit', validateForm);
});
