sub hissatu{
	if ($waza_ritu > int(rand(120))) {
		$dmg1 = ($chara[8] + $chara[33]) * int(rand(20));
		$hpplus1 = $dmg1;
		$sake2 -= 999999;
		$com1 .="<font class=\"dark\" size=4>�Í����@�h���C���I�I�I</font><br>";$kaihuku1 .= "$kname �̂g�o�� $hpplus1 �񕜂����I��";
	}
}
sub atowaza{}
1;