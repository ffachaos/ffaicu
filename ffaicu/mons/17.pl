sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		if (int(rand(1199)) == 0) {
		$sake1 -=999999;
		$dmg1 = 0;
		$dmg2 += int(rand($mrand)) ** 8; 
		$com2 = "<font class=\"red\" size =6>������̊Â������₫�I</font><br>";
		} else {
	$hpplus1 = int(rand($msp)) * 8;
		$kaihuku2 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��";
		$dmg1 = 0;
		$dmg2 = 0;
		$com2 = "<font class=\"yellow\" size=5>�j���̃L�X���</font><br>";
		}
	}
}
sub mons_atowaza{}
1;