import { InfoIcon } from "lucide-react"
import { Button } from "@/components/ui/button"

export function AboutButton() {
    return (
        <Button
            variant="outline"
            className="bg-background border border-gray text-gray-600 hover:white dark:text-gray-200 h-10"
            onClick={() => { }}
        >
            <InfoIcon className="h-[1.2rem] w-[1.2rem]" />
            <span className="sr-only">Toggle theme</span>
        </Button>
    )
}