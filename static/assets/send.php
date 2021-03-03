<?php
$name = $_POST['name'];
$email = $_POST['email'];
$subject = $_POST['subject'];
$message = $_POST['message'];
$fname = htmlspecialchars($fio);
$email = htmlspecialchars($email);
$subject = htmlspecialchars($subject);
$message = htmlspecialchars($message);
$name = urldecode($fio);
$email = urldecode($email);
$subject = urldecode($subject);
$message = urldecode($message);
$name = trim($fio);
$email = trim($email);
$subject = trim($subject);
$message = trim($message);

if (mail("kdmitry2010@yandex.ru", $subject, $message,"From: ".$email))
 {     echo "Ваше сообщение успешно отправлено! Спасибо!";
} else {
    echo "При отправке сообщения возникла ошибка. Повторите попытку";
}?>