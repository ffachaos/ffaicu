sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		if (int(rand(5))==0) {
			$hpplus2 = int(rand($mrand)) * 4;
			$kaihuku2 .= "$mname �̂g�o�� $hpplus2 �񕜂����I��";
			$com2 = "<font class=\"yellow\" size=5>�n�@�n�@�B�B�B</font><br>";
		} else {
			$dmg2 += int(rand($mrand)) * 5;
			$dmg2 += $item[4];
			$sake1 -= 999999;
			$com2 .= "<font class=\"white\" size=5>�n�@�n�@�B�B�B</font><br>";
		}
	}
}
sub mons_atowaza{}
1;