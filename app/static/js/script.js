// Функція для валідації номера телефону
function validatePhoneNumber(phone) {
    // Якщо номер з 12 цифр, він повинен починатися зі знака '+', після якого 12 цифр
    if (phone.length === 13 && phone.startsWith('+')) {
        const phonePattern = /^\+\d{12}$/;
        return phonePattern.test(phone);
    }
    // Якщо номер з 10 цифр, не допускається знак '+'
    else if (phone.length === 10) {
        const phonePattern = /^\d{10}$/;
        return phonePattern.test(phone);
    }
    return false;  // Якщо не відповідає жодному з критеріїв
}

// Функція для валідації імені та прізвища (два слова)

function validateFullName(name) {
    const words = name.trim().split(/\s+/);  // Розділяє по пробілах
    return words.length === 2 && words[0].length > 2 && words[1].length > 2;
}

// Функція для перевірки перед відправкою форми
function validateForm(event) {
    const nameInput = document.querySelector('input[name="name"]');
    const phoneInput = document.querySelector('input[name="phone"]');

    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();

    let isValid = true;

    // Очищаємо помилки перед новою перевіркою
    nameInput.classList.remove('error');
    phoneInput.classList.remove('error');
    nameInput.style.backgroundColor = '';
    phoneInput.style.backgroundColor = '';

    // Перевірка імені та прізвища
    if (!validateFullName(name)) {
        nameInput.style.backgroundColor = '#ffcccc';  // Підсвітити поле червоним фоном
        isValid = false;
    }

    // Перевірка номера телефону
    if (!validatePhoneNumber(phone)) {
        phoneInput.style.backgroundColor = '#ffcccc';  // Підсвітити поле червоним фоном
        isValid = false;
    }

    // Якщо форма валідна, перенаправляємо користувача на іншу сторінку
    if (isValid) {
        window.location.href = "/success";  // Вказати шлях до сторінки для успішної валідації
    } else {
        event.preventDefault();  // Зупиняємо відправку форми, якщо вона не валідна
    }
}

// Додаємо обробник події до форми
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', validateForm);
});
