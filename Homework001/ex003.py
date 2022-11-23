# Напишите программу, которая принимает на вход координаты точки (X и Y),
# X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

Console.Write("Введите число ");
int num = Math.Abs(int.Parse(Console.ReadLine()!));

switch(num)
{
    case 1:
	    Console.WriteLine("x > 0, y > 0");
	    break;
    case 2:
	    Console.WriteLine("x < 0, y > 0");
	    break;
    case 3:
	    Console.WriteLine("x < 0, y < 0");
	    break;
    case 4:
	    Console.WriteLine("x > 0, y < 0");
	    break;
    default:
	    Console.WriteLine("Введено некорректное число");
	    break;
}