# 職業別攻撃時コメント
@battlecom = ("磨き抜かれた剛剣が天地覇王の如く敵を斬り捌くッ！！",
	"古代より生まれし言葉が紅蓮の炎を作り上げ、敵を包むッ！！",
	"汚れ無き心は天に届き、聖なる力が邪なる者を粛正するッ！！",
	"研ぎ澄まされた五感が敵の動きを的確に捉える！！",
	"時空の果てに眠る大いなるマナを呼び覚ます！！",
	"白と黒の魔力が交差して恐るべき力を解放する！！",
	"その美しい音色が刃となり、敵を冥府へと誘う！！",
	"何にも属さぬ稲妻が轟き、敵の生命を絶つッ！！",
	"竜を自在に操る伝説の槍術が敵を貫く！！",
	"聖なる波動が体を包むッ！！ 波動は天の光に姿を変えて敵を焼き焦すッ！！",
	"大いなる父、神の名の元に敵を斬るッ！！",
	"東方より伝わりし剣術、その極意は、一刀両断ッ！！",
	"鼓動が秘めたる力を解放するッ！！ 拳は波動を宿し敵を砕くッ！！",
	"刹那の動きが嵐となり、刃は疾風迅雷の如く敵を斬り捨てるッ！！",
	"負の闘気が剣に宿り、敵を絶望の淵に追いやるッ！！",
	"魔力を込めた剣は紅く光り、全てを斬り裂く衝撃破を発するッ！！",
	"凝縮された魔力が弾丸に込められ敵を撃つッ！！",
	"異世界より呼ばれし者が命を受け、敵を亡き者と化すッ！！",
	"人知越えたを魔力が地球を揺るがすッ！！ 想像を絶する強大な力は全てを破壊するッ！！",
	"魔を滅ぼす伝説の力は邪なる力を封じ込める！！",
	"火・水・土・風・・・全てのアルカナが敵の運命を断ち切る・・・。",
	"まねまね♪",
	"全世界をつなぐネットワークの力を集めて解き放つ！！",
        "あどけない手付きで敵に切りかかる！！・・・こけたｗ",
        "魔物を支配し絶大なる力が敵に襲い掛かる！！",
        "闇より生まれしその存在は気配すら発せず相手を死に至らしめる！！",
        "長い修行で生まれた聖なる力がすべてを浄化する！！",
        "洗練されたその動きは何者も捉えることはできない！！",
        "古の選ばれた聖戦士達が敵に向かい剣をふるう！！",
        "伝説とまで呼ばれたその力は逆らうことすら許さず敵を粉みじんにする！！",
        "この世のすべてを極めし数多の力は神の力にすら匹敵する！！");#コメントここまで

#職業別攻撃力決定サブルーチン名
@iryoku=('syokuzero','syokuone','syokutwo','syokuthree','syokufour','syokufive','syokusix','syokuseven','syokueight','syokunine','syokuten','syokueleven','syokutwelve','syokuthirteen','syokufourteen','syokufifteen','syokusixteen','syokuseventeen','syokueighteen','syokunineteen','syokutwenty','syokutwentyone','syokutwentytwo','syokutwentythree','syokutwentyfour','syokutwentyfive','syokutwentysix','syokutwentyseven','syokutwentyeight','syokutwentynine','syokuthirty');#職業別攻撃力決定ここまで

#------------------#
#　挑戦者の攻撃  　#
#------------------#
sub tyousensya {

	# 挑戦者ダメージ計算
	$com1 = "$chara[4]は、$item[0]で攻撃！！<FONT COLOR=\"$yellow\">$battlecom[$chara[14]]</FONT><br>";

	$attackpower=$iryoku[$chara[14]];
	&$attackpower;

}

#------------------#
#　挑戦者の必殺技　#
#------------------#
sub tyosenwaza {

	# クリティカル
	$waza_ritu = int(($chara[20] / 15)) + 10 + $chara[33];
	if($waza_ritu > 75){$waza_ritu = 75;}
	$waza_ritu += $a_wazaup;
	if($waza_ritu > 95){$waza_ritu = 95;}

	if ($mode eq 'isekiai' or $mode eq 'genei') {
		$waza_ritu = int($waza_ritu / 3);
	}
	elsif ($mode eq 'boss') {
		$waza_ritu = int($waza_ritu / 2);
	}

	#ＨＰが１／１０時に必殺率７５％
	if (int($chara[16] / 10) > $khp_flg && int(rand(4)) > 1) {
		$waza_ritu +=999;
		$com1 .="<font class=\"red\" size=4>LIMIT BREAK!!</font><br>";
	}

	# 封印球の効果
	if ($winner[51] == 19 and $item[7] != 24 and $item[7] != 19) {
		if ($chara[14] > 16 or $mode eq 'boss' or $mode eq 'isekiai') {
			$com2 .="<font color=\"$red\">$winner[27]が光を放つ！！$chara[4] には効かなかった！！</font><br>";
		} elsif ($chara[14] > 7) {
			if (int(rand(5)) == 0) {
				$waza_ritu = 0;
				$com2 .="<font color=\"$yellow\">$winner[27]が光を放つ！！$chara[4] の必殺技を封じ込めた！！</font><br>";
			}
		} else {
			if (int(rand(2)) == 0) {
				$item[7] =0;
				$waza_ritu = 0;
				$com2 .="<font color=\"$yellow\">$winner[27]が光を放つ！！$chara[4] の必殺技を封じ込めた！！</font><br>";
			}
		}
	}

	&hissatu;
}
#------------------#
#　レベルアップ  　#
#------------------#
sub levelup {
	if ($chara[18] < $charamaxlv) {

		# 職業別ボーナス加算処理
		open(IN, "$syoku_file");
		@syoku = <IN>;
		close(IN);

		my ($a, $b, $c, $d, $e, $f, $g, $h, @sy) = split(/<>/, $syoku[$chara[14]]);
		my @as;

		my $base_exp = ($lv_up * ($chara[18] * ($chara[18] - 1))) / 2;
		my $total_exp = $base_exp + $chara[17];

		my $new_level = int((1 + sqrt(1 + (8 * $total_exp) / $lv_up)) / 2);

		my $remaining_exp = $total_exp - ($lv_up * ($new_level * ($new_level - 1))) / 2;

		my $lvup = $new_level - $chara[18];
		$chara[17] = $remaining_exp;
		$chara[18] = $new_level;
		return if $lvup == 0;  # 1回もレベルアップできないなら終了

		# HP の計算
		my $hpup = int(($chara[10] * 3 / 2 + $chara[10]) * $lvup);
		$chara[16] += $hpup;
		$chara[16] = $charamaxhp if $chara[16] > $charamaxhp;
		my $ahp = ($chara[16] > $charamaxhp) ? ($charamaxhp - ($chara[16] - $hpup)) : $hpup;

		foreach my $i (0..$#sy) {
			my $random_factor = 0.8 + rand(1.25 - 0.8);
			$as[$i] = int($sy[$i] * $lvup * $random_factor);
		}

		# ステータスの増加 (まとめて計算)
		$chara[7]  = $charamaxpm if ($chara[7]  += $as[0]) > $charamaxpm;
		$chara[8]  = $charamaxpm if ($chara[8]  += $as[1]) > $charamaxpm;
		$chara[9]  = $charamaxpm if ($chara[9]  += $as[2]) > $charamaxpm;
		$chara[10] = $charamaxpm if ($chara[10] += $as[3]) > $charamaxpm;
		$chara[11] = $charamaxpm if ($chara[11] += $as[4]) > $charamaxpm;
		$chara[12] = $charamaxpm if ($chara[12] += $as[5]) > $charamaxpm;
		$chara[13] = $charamaxpm if ($chara[13] += $as[6]) > $charamaxpm;
		$chara[20] = $charamaxpm if ($chara[20] += $as[7]) > $charamaxpm;

		# レベルアップのメッセージ
		$comment .= "<font class=red size=7>レベルが$lvup上がった！</font><br>";
		my $klvbf = $chara[33];
		$chara[33] += $lvup;
		$chara[33] = 60 if $chara[33] > 60;

		# ジョブマスター処理
		if ($chara[33] > 59 && $klvbf <= 59) {
			$comment .= "<font class=red size=5>$chara_syoku[$chara[14]]をマスターした！！</font><br>";
			my $lock_file = "$lockfolder/syoku$in{'id'}.lock";
			&lock($lock_file, 'SK');
			&syoku_load;
			$syoku_master[$chara[14]] = 60;
			&syoku_regist;
			&unlock($lock_file, 'SK');
		}

		$chara[15] = $chara[16];

		# 各ステータスの増加をコメントに反映
		$comment .= "ＨＰが<font class=yellow>".$ahp."</font>上がった！！" if $ahp;
		$comment .= "力が<font class=yellow>".$as[0]."</font>上がった。" if $as[0];
		$comment .= "魔力が<font class=yellow>".$as[1]."</font>上がった。" if $as[1];
		$comment .= "信仰心が<font class=yellow>".$as[2]."</font>上がった。" if $as[2];
		$comment .= "生命力が<font class=yellow>".$as[3]."</font>上がった。" if $as[3];
		$comment .= "器用さが<font class=yellow>".$as[4]."</font>上がった。" if $as[4];
		$comment .= "速さが<font class=yellow>".$as[5]."</font>上がった。" if $as[5];
		$comment .= "魅力が<font class=yellow>".$as[6]."</font>上がった。" if $as[6];
		$comment .= "カルマが<font class=yellow>".$as[7]."</font>上がった。" if $as[7];

	}
}

#----------------#
# 職業書込み処理 #
#----------------#
sub syoku_regist {

	$new_syoku = '';

	for ($s=0;$s<=$chara[14];$s++) {
		if (!$syoku_master[$s]){
			$syoku_master[$s] = 0;
		}
	}

	$new_syoku = join('<>',@syoku_master);

	$new_syoku .= "<>";

	open(OUT,">./syoku/$in{'id'}.cgi");
	print OUT $new_syoku;
	close(OUT);

}

#------------------#
#挑アクセサリー効果#
#------------------#
sub acs_waza {

	&atowaza;
	&acskouka;

}

#----------------------#
#挑戦者アクセサリー加算#
#----------------------#
sub acs_add {
	$temp_chara[7] = $chara[7];
	$temp_chara[8] = $chara[8];
	$temp_chara[9] = $chara[9];
	$temp_chara[10] = $chara[10];
	$temp_chara[11] = $chara[11];
	$temp_chara[12] = $chara[12];
	$temp_chara[13] = $chara[13];
	$temp_chara[20] = $chara[20];

	$chara[7] += $item[8];
	$chara[8] += $item[9];
	$chara[9] += $item[10];
	$chara[10] += $item[11];
	$chara[11] += $item[12];
	$chara[12] += $item[13];
	$chara[13] += $item[14];
	$chara[20] += $item[15];

	@temp_item = @item;

	if ($chara[30]) {
		require "./tech/$chara[30].pl";
	} else {
		require "./tech/0.pl";
	}
	if ($item[7]) {
		require "./acstech/$item[7].pl";
	} else {
		require "./acstech/0.pl";
	}
}

#--------------------#
#　挑戦者能力値復元　#
#--------------------#
sub acs_sub {
	$chara[7] = $temp_chara[7];
	$chara[8] = $temp_chara[8];
	$chara[9] = $temp_chara[9];
	$chara[10] = $temp_chara[10];
	$chara[11] = $temp_chara[11];
	$chara[12] = $temp_chara[12];
	$chara[13] = $temp_chara[13];
	$chara[20] = $temp_chara[20];
	@item = @temp_item;
}

#--------------------#
#　職業別攻撃力決定　#
#--------------------#
sub syokuzero{
	$dmg1 += int(rand($chara[7])) + $item[1];
}
sub syokuone{
	$dmg1 += int(rand($chara[8])) + $item[1];
}
sub syokutwo{
	$dmg1 += int(rand($chara[9])) + $item[1];
}
sub syokuthree{
	$dmg1 += int(rand($chara[11])) + $item[1];
}
sub syokufour{
	$dmg1 += int(rand($chara[8])) + $item[1];
}
sub syokufive{
	$dmg1 += int(rand($chara[8])) + $item[1];
}
sub syokusix{
	$dmg1 += int(rand($chara[9])) + int(rand($chara[13])) + $item[1];
}
sub syokuseven{
	$dmg1 += int(rand($chara[8])) + int(rand($chara[13])) + $item[1];
}
sub syokueight{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[11])) + $item[1];
}
sub syokunine{
	$dmg1 += int(rand($chara[8])) + int(rand($chara[9])) + $item[1];
}
sub syokuten{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[9])) + $item[1];
}
sub syokueleven{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[8])) + $item[1];
}
sub syokutwelve{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[10])) + $item[1];
}
sub syokuthirteen{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[11])) + $item[1];
}
sub syokufourteen{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[8])) + $item[1];
}
sub syokufifteen{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[8])) + $item[1];
}
sub syokusixteen{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[11])) + $item[1];
}
sub syokuseventeen{
	$dmg1 += int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[13])) + $item[1];
}
sub syokueighteen{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20]) + $item[1];
}
sub syokunineteen{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20]) + $item[1];
}
sub syokutwenty{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20]) + $item[1];
}
sub syokutwentyone{
	$dmg1 += int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20]) + $item[1];
}
sub syokutwentytwo{
	$dmg1 += ((int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20])) * 2) + $item[1];
}
sub syokutwentythree{
	$dmg1 += int(rand($chara[7])) + $item[1];
}
sub syokutwentyfour{
	$dmg1 += ((int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20])) * 2) + $item[1];
}
sub syokutwentyfive{
	$dmg1 += ((int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int((rand($chara[11]))*5) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20])) * 2) + $item[1];
}
sub syokutwentysix{
	$dmg1 += ((int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20])) * 2) + $item[1];
}
sub syokutwentyseven{
	$dmg1 += ((int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20])) * 2) + $item[1];
}
sub syokutwentyeight{
	$dmg1 += ((int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20]))) + $item[1];
}
sub syokutwentynine{
	$dmg1 += ((int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20]))) + $item[1];
}
sub syokuthirty{
	$dmg1 += ((int(rand($chara[7])) + int(rand($chara[8])) + int(rand($chara[9])) + int(rand($chara[10])) + int(rand($chara[11])) + int(rand($chara[12])) + int(rand($chara[13])) + int($chara[20]))) + $item[1];
}#攻撃力計算ここまで

#----------------------#
#　対戦相手データ読替　#
#----------------------#
# キャラデータを@winner_dataに代入してから呼び出すと@winnerに変換します
sub winner_data {

	open(IN,"./item/$winner_data[0].cgi");
	$witem_log = <IN>;
	close(IN);

	@witem = split(/<>/,$witem_log);

	@winner = ($winner_data[0],$winner_data[2],$winner_data[3],$winner_data[4],$winner_data[5],$winner_data[6],$winner_data[7],$winner_data[8],$winner_data[9],$winner_data[10],$winner_data[11],$winner_data[12],$winner_data[13],$winner_data[20],$winner_data[14],$winner_data[15],$winner_data[16],$winner_data[18],$winner_data[21],$winner_data[22],$winner_data[23],$witem[0],$witem[1],$witem[2],$witem[3],$witem[4],$witem[5],$witem[6],$witem[8],$witem[9],$witem[10],$witem[11],$witem[12],$witem[13],$witem[15],$witem[17],$witem[18],$winner_data[30],$winner_data[26],$winner_data[33]);

	$winner[51] = $witem[7];
	$winner[52] = $witem[16];
	$winner[53] = $witem[14];
}
1;
