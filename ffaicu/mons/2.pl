sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		$hpplus2 = int(rand($mhp)) * 2;
		$kaihuku2 .= "$mname �̂g�o�� $hpplus2 �񕜂����I��";
		$dmg2 = 0;
		$com2 = "<font class=\"yellow\" size=5>�����@�P�A���K�I�I�I</font><br>";
	}
}
sub mons_atowaza{}
1;