sub mons_waza{
	if ($mons_ritu > int(rand(100))) {
		$dmg2 += int(rand($mrand));
		$dmg2 += $item[4];
		$sake1 -= 999999;
		$com2 .= "<font class=\"blue\" size=5>黒魔法ブリザガ！！！</font><br>";
	}
}
sub mons_atowaza{}
1;