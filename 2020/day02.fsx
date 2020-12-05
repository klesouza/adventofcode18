type Line = {
    minOccur: int
    maxOccur: int
    letter: string
    pwd: string
}
let parseLine (str: string) =
    let parts = str.Split ' '
    let occurs = parts.[0].Split '-'
    {
        minOccur=int occurs.[0];
        maxOccur=int occurs.[1];
        letter=sprintf "%c" parts.[1].[0];
        pwd=parts.[2];
    }

let day02 (arr: seq<string>) =
    arr
    |> Seq.map parseLine
    |> Seq.filter (fun x ->
        let newpwd = x.pwd.Replace (x.letter, "")
        // printfn "%d %d %d" (x.pwd.Length - newpwd.Length) x.minOccur x.maxOccur
        (x.pwd.Length - newpwd.Length) >= x.minOccur && (x.pwd.Length - newpwd.Length) <= x.maxOccur
    )
    |> Seq.length

let day02p2 (arr: seq<string>) =
    arr
    |> Seq.map parseLine
    |> Seq.filter (fun x ->
        (x.pwd.[x.minOccur-1] = x.letter.[0]) <> ( x.pwd.[x.maxOccur-1] = x.letter.[0])
    )
    |> Seq.length



