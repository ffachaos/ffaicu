sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		$dmg2 += int(rand($mrand));
		$dmg2 += $item[4];
		$hpplus2 = $dmg2;
		$sake1 -= 999999;
		$com2 .= "<font classr=\"dark\" size=4>�Í����@�h���C���I�I�I</font><br>";
		$kaihuku2 .= "$mname �̂g�o�� $hpplus2 �񕜂����I��";
	}
}
sub mons_atowaza{}
1;